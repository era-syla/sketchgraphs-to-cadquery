import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(1.28643, 0.565).lineTo(1.31114, 0.565).lineTo(1.31114, 0.59).lineTo(1.28643, 0.59).lineTo(1.28643, 0.565).close()
solid=wp_sketch0.add(loop0).extrude(0.027941398836544874)
