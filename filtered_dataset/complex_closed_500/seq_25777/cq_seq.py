import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.10454).lineTo(-0.08706, -0.10454).lineTo(-0.08706, 0.06258).lineTo(0.0, 0.06258).lineTo(0.0, -0.10454).close()
solid=wp_sketch0.add(loop0).extrude(-0.4771821660707469)
