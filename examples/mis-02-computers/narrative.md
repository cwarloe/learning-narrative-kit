# The Server in the Feed Room

*Tamarack Supply • MIS Module 2: Computers and Their Business Applications • Hover over highlighted terms for course definitions.*

## Monday, 7:40 a.m.

The propane billing program would not start. Hank Pruitt, the controller, had called Teo Vasquez twice before Teo got his coat off, and the second call was louder than the first. Propane invoices went out on the first business day of the month. It was the first business day of the month.

Dana Okafor followed Teo down the hall because Ruth had told her to learn the server room, and because there wasn't one. There was a closet off the old feed-sample room with a window unit air conditioner, a rack bolted to the cinderblock, and a beige tower on a shelf that everybody called "the billing box."

Teo crouched in front of it. Dana had always assumed it was just a [[computer|computer]], like the one on her desk: something that took data in, ran stored instructions on it without anybody pushing buttons, and put out information. It was that. It was also a [[server|server]], which meant it held the billing program and the shared drives and handed them out to everyone on the network, so when it was sick, everybody was. It was running. Its fans were going. An amber light blinked on the front.

"It's not dead," Teo said. "It's sick."

## What Was Inside the Box

He pulled the side panel off the [[cpu_case|case]] while it ran, which Dana had not known you could do, and pointed with a pen.

The big green board everything plugged into was the [[motherboard|motherboard]]. The square chip under the heat sink was the [[central_processing_unit_cpu|CPU]], which did the actual work. Inside it, he said, there were two parts that mattered for this conversation: the [[control_unit|control unit]], which decided what happened next — fetch this instruction, read that device, send output there — and the [[arithmetic_logic_unit_alu|arithmetic logic unit]], which did the math and the comparisons. Every propane invoice was the ALU multiplying gallons by price and checking whether a balance was greater than zero.

"So the CPU's fine?"

"The CPU's bored. It's waiting." He pointed at four long slots holding memory sticks. "That's [[main_memory|main memory]]. When the billing program runs, it gets loaded into there, into [[random_access_memory_ram|RAM]], because the CPU can read and write it fast. But RAM forgets everything when the power goes off." He tapped the CPU again. "There's also a little [[cache_ram|cache]] right on the processor, so it doesn't have to wait on main memory for stuff it just used. None of that is the problem."

The problem was on the other side of the case: a cage of four hard drives, each one a [[disk_drive|disk drive]], each one built around a spinning [[magnetic_disk|magnetic disk]]. One of them had an amber light of its own.

## Two Dead, One Warning

The four drives were set up as a [[redundant_array_of_independent_disks_rai|RAID]] array. That meant the server spread the data across all four with extra parity information, so that if one drive died, the other three could rebuild what was missing and nobody would notice. That was the point of it. Nobody had noticed.

Teo opened the management console and scrolled back through the log. Drive 2 had failed on February 11. The array had kept running on three drives, exactly as designed, and sent a warning email to an address that belonged to Teo's predecessor. This morning Drive 4 had started throwing read errors. The array could survive one dead disk. It could not reliably survive two. Every time the billing program asked for a record, the request went out across the internal [[bus|bus]] to the drive cage and waited there while Drive 4 tried, failed, and tried again to read its sector. That was why a healthy CPU looked so slow.

"So it's going to lose the data?" Dana asked.

"It's going to try very hard not to, and it's going to be slow while it tries. I'd like it to stop trying."

That left the backups. The [[secondary_memory|secondary memory]] on the drives was where the data was supposed to live when the machine was off; the archival copy was supposed to live somewhere else. Somewhere else turned out to be a cardboard box of [[magnetic_tape|magnetic tape]] cartridges in Hank's office, rotated weekly by Hank's assistant, written by a tape drive on the shelf.

"How long to restore from tape?" Hank asked from the doorway.

Tape stored data sequentially, Teo explained. To get to the billing database, the drive had to wind through everything written before it, and the database was near the end. And nobody had ever done a test restore, so he didn't yet know if the tapes were good.

"Best case, end of day," Teo said. "Worst case, I'll tell you at end of day."

## The Program Nobody Could Change

While the restore ran, Dana asked about the billing program itself, because Hank had said three times that it couldn't be replaced.

It had been written in 2004 by a contractor in Coeur d'Alene who had since retired to Arizona. Teo had the source. He showed her a screen of it.

"This is a [[high_level_languages|high-level language]]," he said. "Which is good news. It's machine independent: the same code would compile on a newer server. The bad news is nobody here reads it."

Dana had taken one programming course. She knew that underneath, everything ran as [[machine_language|machine language]], the zeros and ones a particular processor understood, and that above that sat [[assembly_language|assembly language]], short codes tied to a specific machine. Nobody wrote billing systems in either anymore. The contractor had at least spared them that.

The MSP had sent Teo a quote to rewrite the program. Their proposal was in an [[object_oriented_programming_oop|object-oriented]] language, organized around objects like Customer, Tank, Delivery, and Invoice, each carrying its own data and the actions that went with it. Dana liked the idea of a Tank object that knew its own size. Hank liked nothing that cost forty thousand dollars.

There was a cheaper path. The billing reports Hank actually used each month could be rebuilt in the reporting tool that came with the accounting package, which used a [[fourth_generation_languages_4gls|fourth-generation language]] — one command in place of a page of code. Marcy built her own reports in it. The MSP's sales rep had also pitched an AI assistant that would let Hank "just ask for the report," which Teo described as a [[fifth_generation_languages_5gls|fifth-generation language]] with a subscription fee. Hank said he could already just ask Dana.

## What Should Hold the Data

By two in the afternoon the restore had found the billing database on the third tape and was copying. Teo used the wait to sketch on a whiteboard what should replace the billing box.

Underneath the billing program was the [[operating_system_os|operating system]], which managed the hardware and let the [[application_software|application software]] — billing, the shared drives, the time-clock app — share the machine without fighting over it. That part could move to newer hardware easily. The data was the question.

Option one was [[network_attached_storage_nas|network-attached storage]]: a small dedicated box on the network that did nothing but serve files, with its own RAID inside, and a real alert going to a real person. Cheap, simple, Teo could set it up in a weekend.

Option two was a [[storage_area_network_san|storage area network]], a separate high-speed network just for storage, with shared disk arrays and a proper tape library behind them. That was what the hospital in town ran. It was overkill for eleven stores and it cost more than the rewrite.

"NAS for now," Teo said. "And we test the tapes every quarter. I'm putting that in my calendar and Hank's."

Hank said he didn't want it in his calendar.

## The Ones That Went Out Late

The restore finished at 6:15 p.m. Teo moved the database to a borrowed desktop for the night, on a single plain disk with no RAID behind it, and said so out loud twice so somebody would remember. Dana asked what would happen if the power went out. The desktop would come back up, he said; its startup instructions lived in [[read_only_memory_rom|ROM]] on the motherboard, which kept its contents with the power off and which nothing could write to. Whatever was in RAM at that moment would be gone. Anything not yet saved to the disk would be gone with it.

The billing clerk came back at seven to print. The office printers were fine; the [[output_devices|output devices]] had never been the problem. But the billing program asked for the meter readings from the drivers' handhelds, the [[input_devices|input devices]] that had synced over the weekend, and the weekend's sync had landed on the dying array. Forty-one accounts had readings from the previous month.

Hank made the call: send the rest on time and hold those forty-one for two days. Two of those customers were on a budget plan that drafted automatically, and they would be drafted the wrong amount. Hank wrote their names on a sticky note and put it on his monitor.

Walt approved the NAS on Wednesday and put the rewrite in next year's budget, which in Teo's experience meant the year after. On Friday, Dana found the predecessor's email address in four other alert configurations and changed all of them to a shared IT mailbox. Then she found a fifth, on the router, and sent Teo a list of everything else that still pointed at somebody who didn't work there. He thanked her and didn't open it until the following week.
