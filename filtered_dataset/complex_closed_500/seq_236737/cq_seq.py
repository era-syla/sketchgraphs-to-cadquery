import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.10733, 0.00448).lineTo(-0.03069, 0.00448).lineTo(-0.03069, 0.05536).lineTo(-0.10733, 0.00448).close()
solid=wp_sketch0.add(loop0).extrude(0.2170580519596275)
