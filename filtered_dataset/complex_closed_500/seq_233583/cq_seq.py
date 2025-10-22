import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.5969, 0.71339).lineTo(0.5969, 0.71339).lineTo(0.5969, 0.07128).lineTo(-0.5969, 0.07128).lineTo(-0.5969, 0.71339).close()
solid=wp_sketch0.add(loop0).extrude(-0.7707353107607688)
