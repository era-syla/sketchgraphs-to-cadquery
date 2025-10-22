import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0635, 0.15698).lineTo(0.0635, 0.15698).lineTo(0.0635, 0.13698).lineTo(-0.0635, 0.13698).lineTo(-0.0635, 0.15698).close()
solid=wp_sketch0.add(loop0).extrude(-0.26295679459361204)
