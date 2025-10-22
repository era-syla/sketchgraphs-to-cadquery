import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0719, 0.02384).lineTo(0.07165, 0.02384).lineTo(0.07165, 0.0).lineTo(-0.0719, 0.0).lineTo(-0.0719, 0.02384).close()
solid=wp_sketch0.add(loop0).extrude(-0.1841769047005716)
