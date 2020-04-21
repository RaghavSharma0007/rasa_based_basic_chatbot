## userstroy_success_path_1
* greet
  - utter_greet
  - utter_opportunity_name

> check_account


## userstroy_success_path_1.1
> check_account
> check_hi

* user_opportunity_name{"opportunity_name":"Netsmartz test"}
  - slot{"opportunity_name":"Netsmartz test"}
  - utter_account_name

* user_account_name{"account_name":"Mathew Baynton"}
  - slot{"account_name":"Mathew Baynton"}
  - utter_opportunity_done
  - utter_opportunity_type
  - utter_title

* ask_title_name{"title_name":"Option 1"}
  - slot{"title_name":"Option 1"}
  - utter_state_list
  
* ask_state_name{"state_name":"CA"}
  - slot{"state_name":"CA"}
  - utter_contact
  
* ask_contact_name{"contact_name":"Tim Curry"}
  - slot{"contact_name":"Tim Curry"}
  - utter_pricing
  
* ask_pricing{"pricing":"On Net"}
  - slot{"pricing":"On Net"}
  - utter_estimate
  
* ask_estimate{"estimate_type":"$0 - $50K (3 Days-RVP Approval)"}
  - slot{"estimate_type":"$0 - $50K (3 Days-RVP Approval)"}
  - utter_submit_opp
  
* ask_submit_opp
  - utter_submit_option
  - utter_circuit
   
  
* ask_circuit_type{"circuit_type":"New Circuit"}
  - slot{"circuit_type":"New Circuit"}
  - utter_product
  
* ask_product_type{"product_type":"Bidirectional NNI"}
  - slot{"product_type":"Bidirectional NNI"}
  - utter_bandwidth

* ask_bandwidth{"bandwidth":"500 Gbps"}
  - slot{"bandwidth":"500M"}
  - utter_location_A_a


* ask_location_A_a{"location_A_a":"123 E Marcy St Ste 201, Santa Fe, NM, 87501, Santa Fe Office (Modrall Sperling)"}
  - slot{"location_A_a":"123 E Marcy St Ste 201, Santa Fe, NM, 87501, Santa Fe Office (Modrall Sperling)"}
  - utter_location_Z_z


  
* ask_location_Z_z{"location_Z_z":"123 E Marcy St Ste 201, Santa Fe, NM, 87501, Santa Fe Office (Modrall Sperling)"}
  - slot{"location_Z_z":"123 E Marcy St Ste 201, Santa Fe, NM, 87501, Santa Fe Office (Modrall Sperling)"}
  - utter_submit_circuit
* ask_submit_cir
  - action_submit_cir
  
> check_submit

## userstroy_success_path_1.2
> check_submit
* greet
  - utter_greet
  - utter_account_name
> check_hi
