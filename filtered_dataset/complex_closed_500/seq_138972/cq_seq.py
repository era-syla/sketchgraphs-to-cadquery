import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00762, 0.02231).lineTo(-0.00762, 0.02231).lineTo(-0.00762, 0.00072).lineTo(0.00762, 0.00072).lineTo(0.00762, 0.02231).close()
solid=wp_sketch0.add(loop0).extrude(-0.020916440861182568)
