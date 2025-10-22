import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0425, 0.0425).lineTo(0.0425, 0.0425).lineTo(0.0425, -0.0425).lineTo(-0.0425, -0.0425).lineTo(-0.0425, 0.0425).close()
solid=wp_sketch0.add(loop0).extrude(-0.03732881031095468)
