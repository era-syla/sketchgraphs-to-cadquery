import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0375, 0.00715).lineTo(-0.0345, 0.00715).threePointArc((-0.03662, 0.00627), (-0.0375, 0.00415)).lineTo(-0.0375, -0.00415).threePointArc((-0.03662, -0.00627), (-0.0345, -0.00715)).lineTo(0.0375, -0.00715).threePointArc((0.03962, -0.00627), (0.0405, -0.00415)).lineTo(0.0405, 0.00415).threePointArc((0.03962, 0.00627), (0.0375, 0.00715)).close()
solid=wp_sketch0.add(loop0).extrude(-0.13284492564606393)
