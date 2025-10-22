import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.01).lineTo(0.00719, 0.01).lineTo(0.00719, 0.0).lineTo(0.0, 0.0).lineTo(-0.0, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.002684786038026683)
