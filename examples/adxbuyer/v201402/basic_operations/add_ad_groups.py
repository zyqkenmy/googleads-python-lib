#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example adds ad groups to a given campaign.

To get ad groups, run get_ad_groups.py.

Tags: AdGroupService.mutate
"""

__author__ = 'api.kwinter@gmail.com (Kevin Winter)'

import uuid

from googleads import adwords


CAMPAIGN_ID = 'INSERT_CAMPAIGN_ID_HERE'


def main(client, campaign_id):
  # Initialize appropriate service.
  ad_group_service = client.GetService('AdGroupService', version='v201402')

  # Construct operations and add ad groups.
  operations = [{
      'operator': 'ADD',
      'operand': {
          'campaignId': campaign_id,
          'name': 'Earth to Mars Cruises #%s' % uuid.uuid4(),
          'status': 'ENABLED',
          'biddingStrategyConfiguration': {
              'bids': [
                  {
                      'xsi_type': 'CpmBid',
                      'bid': {
                          'microAmount': '1000000'
                      },
                  }
              ]
          }
      }
  }, {
      'operator': 'ADD',
      'operand': {
          'campaignId': campaign_id,
          'name': 'Earth to Venus Cruises #%s' % uuid.uuid4(),
          'status': 'ENABLED',
          'biddingStrategyConfiguration': {
              'bids': [
                  {
                      'xsi_type': 'CpmBid',
                      'bid': {
                          'microAmount': '1000000'
                      },
                  }
              ]
          }
      }
  }]
  ad_groups = ad_group_service.mutate(operations)

  # Display results.
  for ad_group in ad_groups['value']:
    print ('Ad group with name \'%s\' and id \'%s\' was added.'
           % (ad_group['name'], ad_group['id']))


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, CAMPAIGN_ID)
