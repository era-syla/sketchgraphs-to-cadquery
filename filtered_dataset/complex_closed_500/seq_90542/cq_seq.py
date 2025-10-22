import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.22196).lineTo(0.02, 0.22196).lineTo(0.02, 0.12196).lineTo(-0.02, 0.12196).lineTo(-0.02, 0.22196).close()
solid=wp_sketch0.add(loop0).extrude(-0.2242827117666005)
