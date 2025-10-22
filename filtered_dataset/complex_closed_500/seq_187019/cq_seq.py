import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03, 0.00491).lineTo(0.03, 0.0325).lineTo(0.01, 0.018).lineTo(0.0, 0.018).lineTo(0.0, 0.00491).lineTo(0.03, 0.00491).close()
solid=wp_sketch0.add(loop0).extrude(-0.025129898517311098)
