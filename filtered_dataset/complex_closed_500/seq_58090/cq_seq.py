import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05, -0.05).lineTo(-0.05, -0.05).lineTo(-0.05, 0.05).lineTo(0.05, 0.05).lineTo(0.05, -0.05).close()
solid=wp_sketch0.add(loop0).extrude(0.2869663019737187)
