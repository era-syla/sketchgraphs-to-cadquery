import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.15, -0.02).lineTo(0.02, -0.02).lineTo(0.02, -0.01).lineTo(0.15, -0.01).lineTo(0.15, -0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.1589763608768245)
