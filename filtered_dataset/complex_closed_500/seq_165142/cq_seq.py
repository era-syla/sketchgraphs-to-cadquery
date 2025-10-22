import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00037, -0.16559).threePointArc((0.00244, -0.16164), (0.00353, -0.15691)).lineTo(0.00295, -0.16909).lineTo(-0.00037, -0.16559).close()
solid=wp_sketch0.add(loop0).extrude(-0.0019284924496916823)
