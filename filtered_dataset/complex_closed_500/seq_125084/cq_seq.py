import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(1.2, 0.0).lineTo(1.2, 1.0).lineTo(-0.0, 1.32154).lineTo(-0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-3.205917036623223)
