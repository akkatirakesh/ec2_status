import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="akkatir")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
all_instances_ids=[]
for each_in in ec2_con_re.instances.all():
    all_instances_ids.append(each_in.id)
    print(each_in.id)

while True:
	print("This script performs the following actions on ec2 instance")
	print("""
		1. start
		2. stop
		3. terminate
		4. Exit""")
	opt=int(input("Enter your option: "))

	if opt==1:
            	
            response=ec2_con_cli.describe_instance_status(InstanceIds=["i-0745c0f2ff471a6c5","i-07eccd8e8299f91b8","i-0d73e96965fafd7c9"],IncludeAllInstances=True)
            
            for each in response['InstanceStatuses']:
                value=each['InstanceState']['Name']
                if value=='running':
                   print("Already running " + each['InstanceId'] )
                
                elif value == 'stopped':
                   ec2_stop = ec2_con_cli.start_instances(InstanceIds=[each['InstanceId']])
                   print('starting the instance ' + each['InstanceId'])
                elif value == 'pending':
                   print('pending in progress ' + each['InstanceId'])
                else:
                   print('unknown status')
                
                        
	elif opt==2:
            response=ec2_con_cli.describe_instance_status(InstanceIds=["i-0745c0f2ff471a6c5","i-07eccd8e8299f91b8","i-0d73e96965fafd7c9"],IncludeAllInstances=True)
            for each in response['InstanceStatuses']:
                value=each['InstanceState']['Name']
                if value=='stopped':
                   print("Already stopped " + each['InstanceId'] )
                elif value == 'stopping':
                   print("Stopping in progress " + each['InstanceId'])
                elif value == 'running':
                   ec2_stop = ec2_con_cli.stop_instances(InstanceIds=[each['InstanceId']])
                   print('stopping the instance ' + each['InstanceId'])
                elif value == 'pending':
                   print('can not stop. pending in progress')
                else:
                   print('unknown status')
            
            
	elif opt==3:
            
            print("Terminating ec2 instance.....")
            ec2_con_cli.terminate_instances(InstanceIds=["i-0745c0f2ff471a6c5","i-07eccd8e8299f91b8","i-0d73e96965fafd7c9"])
	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
	else:
	    print("Your option is invalid. Please try once again")