import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.35632, 0.15882).lineTo(0.09368, 0.15882).lineTo(0.09368, 0.14612).lineTo(-0.35632, 0.14612).lineTo(-0.35632, 0.15882).close()
solid=wp_sketch0.add(loop0).extrude(-1.0537151947203498)
