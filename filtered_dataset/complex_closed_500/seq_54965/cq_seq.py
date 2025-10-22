import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00273, -0.056).lineTo(0.00927, -0.056).lineTo(0.00927, 0.00106).lineTo(-0.00273, 0.00106).lineTo(-0.00273, -0.056).close()
solid=wp_sketch0.add(loop0).extrude(0.07389487606089548)
