import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00735, 0.00875).lineTo(0.00628, 0.00522).lineTo(0.00376, 0.00252).lineTo(0.0047, 0.00198).lineTo(0.0083, 0.00821).lineTo(0.00735, 0.00875).close()
solid=wp_sketch0.add(loop0).extrude(0.0033884400350355664)
