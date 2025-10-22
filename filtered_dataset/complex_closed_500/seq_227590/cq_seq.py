import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02413, -0.01651).lineTo(-0.02413, -0.01651).lineTo(-0.02413, 0.01651).lineTo(0.02413, 0.01651).lineTo(0.02413, -0.01651).close()
solid=wp_sketch0.add(loop0).extrude(0.018065785327438733)
