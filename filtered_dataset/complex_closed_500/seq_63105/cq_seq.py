import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06492, 0.0).lineTo(0.01128, 0.0).lineTo(0.01128, 0.0254).lineTo(-0.01412, 0.0254).lineTo(-0.01412, 0.0762).lineTo(-0.03952, 0.0762).lineTo(-0.03952, 0.0254).lineTo(-0.06492, 0.0254).lineTo(-0.06492, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.055092605298958514)
