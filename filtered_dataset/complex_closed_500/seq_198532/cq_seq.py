import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01722, 0.00454).lineTo(0.00978, 0.00454).lineTo(0.00978, -0.00546).lineTo(-0.01722, -0.00546).lineTo(-0.01722, 0.00454).close()
solid=wp_sketch0.add(loop0).extrude(0.0029004677511999064)
