import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0085, 0.0387).lineTo(-0.0405, 0.0387).lineTo(-0.0405, 0.0317).lineTo(-0.0085, 0.0317).lineTo(-0.0085, 0.0387).close()
solid=wp_sketch0.add(loop0).extrude(-0.0016613579399325999)
