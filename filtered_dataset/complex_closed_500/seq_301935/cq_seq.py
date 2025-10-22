import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05172, 0.0).lineTo(-0.04172, 0.0).lineTo(-0.04172, 0.2).lineTo(-0.05172, 0.2).lineTo(-0.05172, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.32184896783700023)
