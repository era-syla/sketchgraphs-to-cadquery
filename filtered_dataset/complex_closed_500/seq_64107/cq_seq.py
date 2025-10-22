import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00665, 0.016).lineTo(-0.0078, 0.016).lineTo(-0.0078, -0.0).lineTo(-0.00665, -0.0).lineTo(-0.00665, 0.016).close()
solid=wp_sketch0.add(loop0).extrude(0.0011125798425766788)
