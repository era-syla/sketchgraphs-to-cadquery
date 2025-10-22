import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03865, 0.00224).threePointArc((0.04089, 0.0), (0.03865, -0.00224)).lineTo(0.03051, -0.00224).threePointArc((0.02827, -0.0), (0.03051, 0.00224)).lineTo(0.03865, 0.00224).close()
solid=wp_sketch0.add(loop0).extrude(-0.014865041613653521)
