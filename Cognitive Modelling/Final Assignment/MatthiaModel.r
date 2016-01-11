#Cognitive Modelling Final Assignment
#Msc Artificial Intelligence 
#Matthia Sabatelli, S2847485

#Integration of Timing Module and Declarative Memory system

#5 blocks, different blocks had different predominant stimuli
#blocks 1 3 5 durations were equally presented 400 800 1200 1600, blocks 2 4 had namely more longer 1600 or shorter stimuli 400
#exponential session (shorter) 64 32 16 8 ---> 400 800 1200 1600 
#antiexponential session (longer) 8 16 32 64 ---> 400 800 1200 1600
 
#Implement Blending!!!!!


actr.a = 1.1
actr.b = 0.015
actr.t0 = 1.1

num.subjects = 18 #number of participants? 18 according to the data we have
num.sessions = 5
num.trials = 120

foreperiods = c(400, 800, 1200, 1600)

printf <- function(...) print(sprintf(...))

plot.experiment.data <- function()
{

	#read .csv file with data experiment


}


create.dm <- function(chunks,encounters)
{
  if (chunks > 52)
  {
    stop("Only up to 52 chunks allowed.")
  }
  DM <- array(NA,c(chunks,encounters))
  row.names(DM) <- c(letters,LETTERS)[1:chunks]
  
  return (DM)
}

add.encounter <- function(DM,chunk,time)
{
  tmp <- DM[chunk,]
  DM[chunk,sum(!is.na(tmp))+1] <- time
  
  return (DM)
}

get.encounters <- function(DM,chunk)
{
  tmp <- DM[chunk,]
  tmp[!is.na(tmp)]
}

actr.B <- function(encounters,curtime)
{
  if (curtime < min(encounters))
  {
    return(NA)
  }
  else
  {
    log(sum((curtime - encounters[encounters<curtime])^-params$d))
  }
}


actr.noise <- function(s,n=1)
{
  rand <- runif(n,min=0.0001,max=0.9999)
  s * log((1 - rand ) / rand)
}

pulse_into_time <- function(num_pulses)
{
  interval_estimation <- actr.t0
  global_time <- actr.t0
  
  for (i in 1:num_pulses)
  {
    interval_estimation <- interval_estimation * actr.a + actr.noise(actr.a * actr.b* interval_estimation)
    global_time <- global_time + interval_estimation
  }
  
  return (global_time)
  
}

time_into_pulse <- function(time)
{
  interval_estimation <- actr.t0
  num_pulses <- 0
  time_tracker <- actr.t0
  
  while(time_tracker < time)
  {
    interval_estimation <- interval_estimation * actr.a + actr.noise(actr.a * actr.b* interval_estimation)
    time_tracker <-  time_tracker + interval_estimation
    num_pulses <- num_pulses +1
  }
  
  return (num_pulses)
  
}

run_session <- function(list.params)
{

}

run_model <- function()
{
	for(i in 1:num.sessions)
	{
		condition <- sample(1:5,1)
		
		if (condition == 1)
		{
			run_session(#classic_params)
		}
		
		else if (condition == 2)
		{	
			
			run_session(#antiexpoparams)
		}

		else if (condition == 4)
		{
			run_session(#expo params)
		}

		else
		{
			run_session(#classic_params)
		}

	}	
	
}


my_main <- function()
{
	
}

my_main()


