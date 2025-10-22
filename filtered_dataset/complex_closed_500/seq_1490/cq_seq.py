import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(11.44941, 2.4).lineTo(11.54941, 2.3).lineTo(11.6073, 2.3).lineTo(11.6073, 2.4).lineTo(11.44941, 2.4).close()
solid=wp_sketch0.add(loop0).extrude(0.06162013006951584)
