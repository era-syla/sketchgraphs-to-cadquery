import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.225, 0.1).lineTo(-0.225, 0.1).lineTo(-0.225, -0.1).lineTo(0.225, -0.1).lineTo(0.225, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(1.087563070122189)
