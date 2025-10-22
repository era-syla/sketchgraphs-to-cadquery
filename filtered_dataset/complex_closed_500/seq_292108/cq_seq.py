import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.018, 0.0).lineTo(-0.018, -0.005).lineTo(-0.005, -0.005).lineTo(-0.005, -0.018).lineTo(0.0, -0.018).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0427537158996602)
