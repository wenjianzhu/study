* 为什么使用消息队列？
	* 使用消息队列的三个好处： 解耦、异步、削峰
	*  **解耦**
		* 比如A系统有一个请求要发送到B系统，C系统，A系统写了两段发送请求的逻辑，但是后面又需要增加一个D系统，前面C系统又不需要请求了，这时候必须修改A系统的代码，这样耦合性就很强，这时候就可以使用消息队列，A系统把请求发送到消息队列里面去，然后其他几个系统如果需要请求，就直接去消息队列里面消费就好了，反之如果不需要请求了， 那就取消消费就可以了，这样就降低了耦合，A系统只需要把请求放到消息队列里面去就可以了
	* **异步**
		* 举个例子 如果用户发送一个请求到了A系统需要20ms 然后A系统再分别发送请求到BCD三个系统需要 200ms ，300ms ，350ms ，这样一来用户发送一个请求一共要差不多一秒才能获得响应，这样是很不友好的，如果使用消息队列，A系统发送3条消息到需要10ms 然后加上用户请求A系统需要20ms  一共就是30ms用户就得到了响应，用户体验是很好的
	* **削峰**
		* 

* 使用消息队列的好处和坏处
* Kafka、ActiveMQ、RabbitMQ、RocketMQ 都有什么区别，以及适合哪些场景？