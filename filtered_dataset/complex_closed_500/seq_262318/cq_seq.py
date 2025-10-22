import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00945, 0.0099).lineTo(-0.00115, 0.0099).lineTo(-0.00115, 0.0066).lineTo(-0.00945, 0.0066).lineTo(-0.00945, 0.0099).close()
solid=wp_sketch0.add(loop0).extrude(-0.013786294818486046)
