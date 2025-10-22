import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.52206, 0.84512).lineTo(1.56889, 0.84512).threePointArc((1.58657, 0.85245), (1.59389, 0.87012)).lineTo(1.59389, 0.96226).threePointArc((1.58657, 0.97994), (1.56889, 0.98726)).lineTo(1.52206, 0.98726).threePointArc((1.4867, 0.97262), (1.47206, 0.93726)).lineTo(1.47206, 0.89512).threePointArc((1.4867, 0.85977), (1.52206, 0.84512)).close()
solid=wp_sketch0.add(loop0).extrude(0.20693370235428316)
