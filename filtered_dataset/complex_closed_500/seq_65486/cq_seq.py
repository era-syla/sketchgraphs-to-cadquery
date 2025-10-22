import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.23633, -0.74608).lineTo(1.26173, -0.74608).lineTo(1.26173, -0.69528).lineTo(1.23633, -0.69528).lineTo(1.23633, -0.74608).close()
solid=wp_sketch0.add(loop0).extrude(-0.0008373235660593853)
