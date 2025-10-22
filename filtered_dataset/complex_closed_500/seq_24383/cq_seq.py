import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.4594, -0.30977).lineTo(0.1502, -0.30977).lineTo(0.1502, 0.29983).lineTo(-0.4594, 0.29983).lineTo(-0.4594, -0.30977).close()
solid=wp_sketch0.add(loop0).extrude(-1.1322619516905732)
