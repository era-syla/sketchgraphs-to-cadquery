import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0133, 0.00454).lineTo(0.0093, 0.00454).lineTo(0.0093, 0.02454).lineTo(0.0133, 0.02454).lineTo(0.0133, 0.00454).close()
solid=wp_sketch0.add(loop0).extrude(0.055305055914668735)
