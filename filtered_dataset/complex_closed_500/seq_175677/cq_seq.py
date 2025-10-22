import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0381, 0.14605).lineTo(-3.0861, 0.14605).lineTo(-3.0861, 2.92735).lineTo(0.0381, 2.92735).lineTo(0.0381, 0.14605).close()
solid=wp_sketch0.add(loop0).extrude(-6.519941191078096)
