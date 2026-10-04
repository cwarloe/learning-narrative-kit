# The Closet Gets Too Hot

*Tamarack Feed & Supply Co. • MIS Module 10: Emerging Trends, Technologies, and Applications • Hover over highlighted terms for course definitions.*

## Ninety-Seven Degrees

In the second week of July, the window air conditioner in the feed-room closet quit during a heat wave, and by two in the afternoon the thermometer Teo Vasquez had taped to the rack read ninety-seven degrees. The new NAS shut itself down to protect its disks. The billing program, the shared drives, and the time clock went with it.

Teo got a portable cooler from the DC and had everything back up by four. Then he went to Ruth Halvorsen's office and said what he'd been saying since the spring: Tamarack shouldn't be running its own servers in a closet.

Ruth agreed, mostly. She had a problem of her own. The ERP selection had started, and every vendor on the shortlist was asking where Tamarack wanted the system to run. She told Teo to bring her a recommendation in two weeks, with costs, and to take Dana Okafor with him to the farm-retail technology expo in Boise, because half the vendors would be there.

## What "The Cloud" Was Being Sold As

On the first morning at the expo, Dana counted fourteen booths with the word "cloud" on their banners. She and Teo spent the day sorting what they actually meant.

[[cloud_computing|Cloud computing]] in general meant using one platform to deliver many technologies over the Internet, with business applications accessed through a browser and data kept on the provider's servers. The question was which layer Tamarack would rent.

At the bottom was [[infrastructure_as_a_service_iaas|infrastructure as a service]]: renting servers, storage, and networking from a provider and running Tamarack's own software on them. That was the closest to what Teo did now, minus the closet. Above that was [[platform_as_a_service_paas|platform as a service]], which gave developers a ready environment to build applications in. Nobody at Tamarack built applications, but the MSP that might rewrite the propane billing program would.

At the top was [[software_as_a_service_saas|software as a service]]: the vendor ran the whole application and Tamarack used it through a browser for a fee. Two of the three ERP vendors sold only that way. One booth called it [[on_demand_software|on-demand software]], another called it [[software_as_a_service|Software as a Service]], and both meant a subscription, monthly or annual, instead of a license Tamarack owned. The old term for the companies doing it was [[application_service_providers_asps|application service providers]], which one of the older salespeople still used.

"So we stop owning things," Dana said.

"We stop owning servers," Teo said. "We rent everything else. Forever."

## Whose Cloud

The second sorting question was where the cloud lived.

A [[public_cloud|public cloud]] meant connecting over the Internet to a provider's off-site infrastructure, shared with its other customers. A [[private_cloud|private cloud]] ran the same kind of services on a private network for one organization. That was what a hospital system Teo knew had built, and it was far beyond Tamarack's budget. A [[hybrid_cloud|hybrid cloud]] combined at least one of each.

One booth was run by the regional farm-supply dealers' association. It was offering a [[community_cloud|community cloud]], infrastructure built for the exclusive use of a group of organizations with shared concerns: in this case, farm-supply dealers who needed the same compliance rules for pesticide sales records and wanted to share purchasing data. Dana recognized two of the dealers on the member list. They were the same ones Marcy had wanted to form a buying group with in the winter.

Teo also heard the word [[multicloud|multicloud]] at three booths. It meant using more than one public cloud. Teo pointed out that Tamarack would be multicloud by accident the day it signed the ERP contract, since the web store, the loyalty program, and Counter Assistant each already lived in a different provider's cloud.

## The Stores and the Wire

The vendor Teo liked best spent twenty minutes on the question Teo was most worried about: the stores' internet.

If Tamarack's registers depended on a cloud system in a data center in Oregon, every sale at the Republic store would cross a rural internet connection that went down a few times each winter. The vendor's answer was [[edge_computing|edge computing]]: keep processing and data close to where it was used, at the edge of the network, so a store could keep ringing sales during an outage and sync later. That was what Teo had wanted from the distributed database idea in the spring.

A larger provider pitched [[distributed_cloud_computing|distributed cloud computing]], spreading its cloud services to physical locations closer to the users so data didn't have to travel to Oregon and back. Its nearest location was Seattle. That helped head office. It didn't help Republic.

## Paying by the Hour

The pricing models were their own sorting job.

[[utility_on_demand_computing|Utility computing]] meant paying for computing and storage as you used them, like electricity. Teo liked that for the propane route optimizer from the spring trial, which needed a great deal of computing power for an hour a week and none the rest of the time. One vendor proposed running it on [[grid_computing|grid computing]] instead, combining the processing power of many computers across a network to solve one large problem faster than a single machine could.

[[cloud_storage|Cloud storage]] meant leasing space on servers run by a third party, sized to current or future needs. [[backup_as_a_service_baas|Backup as a service]] meant offsite storage for files or entire drives, so the next failed disk wouldn't mean a day of rewinding tapes. Teo signed up for a trial on the spot.

[[data_as_a_service_daas|Data as a service]] bundled storage, integration, processing, and analytics. Dana noticed it was the merchandising data mart from the spring, rented instead of built. [[security_as_a_service_secaas|Security as a service]] sold cybersecurity monitoring by subscription. After the payment fraud, Hank Pruitt would have signed anything with that label, so Dana kept the brochure away from him.

## The Other Halls

The expo's second hall was where vendors went when they didn't have a product yet. Walt Brandvold drove down for the second day and spent most of it there.

A cattle association was promoting a [[blockchain|blockchain]] for beef traceability: a decentralized network that recorded every transaction — calf born, sold, vaccinated, shipped — as blocks that couldn't be altered once written. They wanted feed dealers to record feed lots on it so a rancher could prove what their cattle had eaten. They were building it on [[blockchain_as_a_service_baas|blockchain as a service]], cloud infrastructure from a third party designed for organizations building their own blockchains. Walt was interested. Dana asked who paid for each record. The answer was each participant, per transaction.

A different booth wanted to let customers pay in [[cryptocurrency|cryptocurrency]], digital money created from computer code and tracked by a peer-to-peer network. Hank had already said no to this once, when a rancher asked.

The same booth was selling a loyalty-points program on a blockchain. Its points were [[fungible_tokens|fungible tokens]], each one interchangeable with any other, like dollars. Its "Founders' Herd" collectibles were [[non_fungible_token_nft|non-fungible tokens]], each one unique, with a different digital cow painting on each. Its event passes for the county fair were [[semi_fungible_tokens_sfts|semi-fungible tokens]]: interchangeable as admission until the fair ended, then unique souvenirs. Walt bought nothing and said the cow paintings were ugly.

## Seeing What Isn't There

The training booths were the ones Eli Mendez would have liked, and Dana took pictures for him.

A forklift manufacturer offered [[virtual_reality_vr|virtual reality]] training: a headset with computer-generated 3D scenes that made a new driver feel like they were in a real DC. In the full headset, the driver was in an [[egocentric_environment|egocentric environment]], completely immersed. A cheaper version ran on a laptop as an [[exocentric_environment|exocentric environment]], a window view in 3D where the trainee could watch but not reach in and move things. A university booth had a [[cave_automatic_virtual_environment_cave|CAVE]], a cube-shaped room with rear-projection screens for walls and true 3D images, for designing grain-handling facilities. It cost more than the twelfth store.

A fencing company had an [[augmented_reality_ar|augmented reality]] app: point a phone at a pasture and it laid a virtual fence line over the real ground, with a count of posts and rolls. A step further was [[mixed_reality_mr|mixed reality]], where the virtual fence was anchored to real objects and responded to them, so a virtual gate would swing and stop against a real post. Marcy would have wanted the AR app for the web store tomorrow.

One feed brand had built a [[virtual_world|virtual world]], a simulated farm where customers interacted with each other through [[avatar|avatars]] and could shop for feed. The brand's rep said it was their first step into the [[metaverse|metaverse]], a 3D virtual world where people could do most of what they did in the real one. The virtual farm had four visitors while Dana watched, and three of them were the rep's colleagues.

## Things That Were Coming Anyway

Some of what they saw would reach Tamarack whether Tamarack chose it or not.

A parts supplier demonstrated [[3d_printing|3D printing]], building a replacement gear for a discontinued grain-cart model one thin layer at a time from a digital file. Ranchers brought that kind of problem to the counter every week. A research booth showed [[4d_printing|4D printing]], printed objects made of materials programmed to change shape with heat or moisture, like an irrigation valve that opened itself when the soil dried. A fencing-wire maker talked about [[nanotechnology|nanotechnology]] coatings, engineered at the scale of molecules, that it claimed would double galvanized wire's life. Dana wrote down the claim and not the number.

A loyalty-app vendor demonstrated [[contextual_computing|contextual computing]]: an app that knew a customer had walked into the store, knew what they'd bought last spring, and suggested a refill. Dana thought about the GDPR request and didn't sign up.

One small booth was selling [[implanted_microchips|implanted microchips]] for people: chips the size of a rice grain, implanted in the hand, that could hold ID and payment information. Walt pointed out that Tamarack already sold microchips — for horses. He did not stop at the booth.

The keynote speaker talked about [[quantum_computing|quantum computing]], computers using qubits to solve problems traditional ones couldn't. The speaker said it would someday break today's encryption. Teo said he would add it to the list after zero trust.

The cheapest thing Dana saw at the whole expo was a [[qr_quick_response_code|QR code]], a square matrix barcode, printed on a feed-bag tag. Scanning it opened the product's feeding guide. Dana thought it could open Counter Assistant's explanation for that product. It would cost almost nothing.

## The Recommendation

Teo's recommendation to Ruth was a hybrid. The ERP would be SaaS in a public cloud. Each store would keep an edge server so registers could run offline. Backups would go to a backup-as-a-service provider, and the closet would hold only network equipment. The billing program would move to rented infrastructure until it was rewritten. Tamarack would join the dealers' community cloud for pesticide records only.

Ruth approved it. Hank asked what the monthly bill would be, and when Teo told him, asked what they'd been paying for the closet. Teo said nothing, except when it failed. Hank said that was his point.

The migration was planned for the fall. The QR codes went on the feed tags in September. In October the Republic store's internet went down for six hours during the first snow, and its edge server, which had been installed only two weeks earlier, kept the registers running until the line came back. Then it took eleven hours to sync, and two loyalty customers got double points.
