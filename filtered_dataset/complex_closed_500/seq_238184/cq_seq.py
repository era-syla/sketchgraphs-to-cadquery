import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00275, 0.03625).lineTo(0.00275, 0.03625).lineTo(0.00275, 0.03425).lineTo(-0.00275, 0.03425).lineTo(-0.00275, 0.03625).close()
solid=wp_sketch0.add(loop0).extrude(-0.013950952237404534)
