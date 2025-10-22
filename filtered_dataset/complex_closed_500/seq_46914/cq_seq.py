import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0635, 0.045).lineTo(-0.0585, 0.045).lineTo(-0.05295, 0.01328).threePointArc((-0.04953, 0.00734), (-0.0431, 0.005)).lineTo(0.0431, 0.005).threePointArc((0.04953, 0.00734), (0.05295, 0.01328)).lineTo(0.0585, 0.045).lineTo(0.0635, 0.045).lineTo(0.0635, 0.0).lineTo(-0.0635, 0.0).lineTo(-0.0635, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(-0.08776165351498354)
