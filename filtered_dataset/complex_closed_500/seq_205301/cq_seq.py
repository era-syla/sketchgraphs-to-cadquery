import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.7, 0.028).lineTo(1.5, 0.028).lineTo(1.5, 0.155).lineTo(0.7, 0.155).lineTo(0.7, 0.028).close()
solid=wp_sketch0.add(loop0).extrude(1.1610633784225228)
