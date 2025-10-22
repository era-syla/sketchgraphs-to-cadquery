import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.122, 0.0625).lineTo(-0.122, 0.0625).threePointArc((-0.12412, 0.06162), (-0.125, 0.0595)).lineTo(-0.125, -0.0595).threePointArc((-0.12412, -0.06162), (-0.122, -0.0625)).lineTo(0.122, -0.0625).threePointArc((0.12412, -0.06162), (0.125, -0.0595)).lineTo(0.125, 0.0595).threePointArc((0.12412, 0.06162), (0.122, 0.0625)).close()
solid=wp_sketch0.add(loop0).extrude(0.7328235723249632)
