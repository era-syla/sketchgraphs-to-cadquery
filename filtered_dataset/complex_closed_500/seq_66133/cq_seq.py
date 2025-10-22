import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.126, 0.005).threePointArc((-0.131, 0.0), (-0.126, -0.005)).lineTo(-0.126, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.022873142509004428)
