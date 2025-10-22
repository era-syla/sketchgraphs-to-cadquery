import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03048, 0.03198).lineTo(-0.01048, 0.03198).lineTo(-0.01048, 0.00198).lineTo(-0.03048, 0.00198).lineTo(-0.03048, 0.03198).close()
solid=wp_sketch0.add(loop0).extrude(-0.0758420454353149)
