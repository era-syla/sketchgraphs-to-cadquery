import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00175, 0.01621).lineTo(-0.00175, 0.01621).lineTo(-0.00175, 0.01971).lineTo(0.00175, 0.01971).lineTo(0.00175, 0.01621).close()
solid=wp_sketch0.add(loop0).extrude(0.0025988309310515253)
