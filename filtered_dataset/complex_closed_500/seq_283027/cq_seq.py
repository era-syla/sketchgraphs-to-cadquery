import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0337, 0.0).lineTo(-0.0233, 0.0).lineTo(-0.0233, 0.016).lineTo(0.0337, 0.016).lineTo(0.0337, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.02555827484723666)
