import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07191, 0.01651).lineTo(0.04877, 0.01651).lineTo(0.04877, 0.01634).lineTo(-0.07191, 0.01634).lineTo(-0.07191, 0.01651).close()
solid=wp_sketch0.add(loop0).extrude(0.16424925567114287)
