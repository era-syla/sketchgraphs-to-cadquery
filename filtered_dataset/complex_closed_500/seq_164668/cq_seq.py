import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00987, 0.03866).lineTo(-0.00292, 0.03949).lineTo(-0.00248, 0.03579).lineTo(-0.00943, 0.03496).lineTo(-0.00987, 0.03866).close()
solid=wp_sketch0.add(loop0).extrude(-0.016509678114371065)
