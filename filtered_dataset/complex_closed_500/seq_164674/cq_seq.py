import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02502, 0.02652).lineTo(0.02222, 0.02652).lineTo(0.02222, 0.02153).lineTo(0.02502, 0.02153).lineTo(0.02502, 0.02652).close()
solid=wp_sketch0.add(loop0).extrude(0.012999439847459755)
