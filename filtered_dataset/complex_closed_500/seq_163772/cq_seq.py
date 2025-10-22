import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-45.65567, 21.5224).lineTo(-38.03567, 21.5224).lineTo(-38.03567, 6.2824).lineTo(-45.65567, 6.2824).lineTo(-45.65567, 21.5224).close()
solid=wp_sketch0.add(loop0).extrude(2.312564631263586)
